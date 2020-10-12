CMAKE_MINIMUM_REQUIRED(VERSION 2.8.7)
PROJECT(Nektar++-Tutorial)

INCLUDE(CMakeParseArguments)

SET(TUTORIAL_ROOT ${CMAKE_CURRENT_SOURCE_DIR})

ADD_CUSTOM_TARGET(tutorials)
ADD_CUSTOM_TARGET(tutorials-pdf)
ADD_CUSTOM_TARGET(tutorials-html)
ADD_DEPENDENCIES(tutorials tutorials-pdf tutorials-html)

# Generates PDF and HTML targets for tutorials. These will be named
# <target-base-name>-pdf and <target-base-name>-html.
#
# TARGET <name>         Base name of target to create.
# BASE <name>           Base name of .tex file.
# STYLING_FILE <file>   The HTML styling file to use.
# PDF                   Generate PDF target.
# HTML                  Generate HTML target.
# HTML_BREAK_LEVEL <N>  Section depth to break into separate files.
# USES_INDEX            Run 'makeindex'
# USES_REFS             Run 'bibtex'
# ARCHIVE               Make tarball of associated files
#                       First file is archive name, followed by included files.
#
MACRO(ADD_NEKTAR_TUTORIAL)
    SET(options PDF HTML USES_INDEX USES_REFS)
    SET(oneValueArgs TARGET BASE STYLING_FILE HTML_BREAK_LEVEL)
    SET(multiValueArgs ARCHIVE)
    cmake_parse_arguments(NEK "${options}"
        "${oneValueArgs}" "${multiValueArgs}" ${ARGN} )

    SET(NEKSRC ${CMAKE_SOURCE_DIR})
    SET(SRC ${CMAKE_CURRENT_SOURCE_DIR})
    SET(TGT ${CMAKE_CURRENT_BINARY_DIR})

    IF (NEK_PDF)
        FIND_PROGRAM(PDFLATEX  pdflatex)
        FIND_PROGRAM(BIBTEX    bibtex)
        FIND_PROGRAM(MAKEINDEX makeindex)
        MARK_AS_ADVANCED(PDFLATEX BIBTEX MAKEINDEX)

        # Main target (Final PDFLatex)
        ADD_CUSTOM_TARGET(${NEK_TARGET}-pdf
            TEXINPUTS=${NEKSRC}/:${TUTORIAL_ROOT}/shared//:
            ${PDFLATEX} --output-directory ${TGT} ${SRC}/${NEK_BASE}.tex
            WORKING_DIRECTORY ${SRC}
        )

        # Initial PDFLATEX
        ADD_CUSTOM_TARGET(${NEK_TARGET}-pdflatex
            TEXINPUTS=${NEKSRC}/:${TUTORIAL_ROOT}/shared//:
            ${PDFLATEX} --output-directory ${TGT} ${SRC}/${NEK_BASE}.tex
            WORKING_DIRECTORY ${SRC})
        ADD_DEPENDENCIES(${NEK_TARGET}-pdf ${NEK_TARGET}-pdflatex)

        # Bibtex if required
        IF (NEK_USES_REFS)
            ADD_CUSTOM_TARGET(${NEK_TARGET}-bibtex
                COMMAND TEXMFOUTPUT=${TGT} ${BIBTEX} ${TGT}/${NEK_BASE}.aux
                WORKING_DIRECTORY ${SRC})
            ADD_DEPENDENCIES(${NEK_TARGET}-pdf ${NEK_TARGET}-bibtex)
            ADD_DEPENDENCIES(${NEK_TARGET}-bibtex ${NEK_TARGET}-pdflatex)
        ENDIF()

        # Index if required
        IF (NEK_USES_INDEX)
            ADD_CUSTOM_TARGET(${NEK_TARGET}-index
                COMMAND TEXMFOUTPUT=${TGT} ${MAKEINDEX} ${TGT}/${NEK_BASE}.aux
                WORKING_DIRECTORY ${SRC})
            ADD_DEPENDENCIES(${NEK_TARGET}-pdf ${NEK_TARGET}-index)
            ADD_DEPENDENCIES(${NEK_TARGET}-index ${NEK_TARGET}-pdflatex)
        ENDIF()

        # Create an archive of the tutorial files
        IF (NEK_ARCHIVE)
            SET(TARFILE "${TGT}/${NEK_TARGET}.tar.gz")
            ADD_CUSTOM_COMMAND(TARGET ${NEK_TARGET}-pdf POST_BUILD
                COMMAND ${CMAKE_COMMAND} -E tar "cvfz" ${TARFILE}
                    ${NEK_ARCHIVE}
                WORKING_DIRECTORY ${SRC}
                COMMENT "Generating ${TARFILE}")
        ENDIF()

        # Install resulting files if generated.
        INSTALL(CODE "IF (EXISTS ${TGT}/${NEK_BASE}.pdf)
                FILE(INSTALL ${TGT}/${NEK_BASE}.pdf
                DESTINATION \${CMAKE_INSTALL_PREFIX}/${NEKTAR_DOC_DIR}/tutorials/${NEK_TARGET})
             ENDIF()")

        ADD_DEPENDENCIES(tutorials-pdf ${NEK_TARGET}-pdf)
    ENDIF ()

    IF (NEK_HTML)
        FILE(MAKE_DIRECTORY ${TGT}/html)

        FIND_PROGRAM(HTLATEX htlatex)
        MARK_AS_ADVANCED(HTLATEX)

        IF (NOT NEK_HTML_BREAK_LEVEL)
            SET(NEK_HTML_BREAK_LEVEL 3)
        ENDIF()

        # Generate HTML
        SET(FLAGS "html,${NEK_HTML_BREAK_LEVEL},next,NoFonts")
        IF (NEK_STYLING_FILE)
            SET(FLAGS "${NEK_STYLING_FILE},${FLAGS}")
        ENDIF()

        ADD_CUSTOM_TARGET(${NEK_TARGET}-html
            TEXINPUTS=${NEKSRC}/:${SRC}//:${TUTORIAL_ROOT}/shared//:
            ${HTLATEX} ${SRC}/${NEK_BASE}.tex
            "${FLAGS}"
            WORKING_DIRECTORY ${TGT}/html
        )

        # Copy images across
        FILE(GLOB_RECURSE imgfiles "img/*.png" "img/*.jpg" "*/img/*.png"
            "*/img/*.jpg" "${TUTORIAL_ROOT}/shared/img/*.png"
            "${TUTORIAL_ROOT}/shared/img/*.jpg")
        ADD_CUSTOM_COMMAND(TARGET ${NEK_TARGET}-html POST_BUILD
            COMMAND ${CMAKE_COMMAND} -E make_directory ${TGT}/html/img)
        FOREACH(img ${imgfiles})
            ADD_CUSTOM_COMMAND(TARGET ${NEK_TARGET}-html POST_BUILD
                COMMAND ${CMAKE_COMMAND} -E copy ${img} ${TGT}/html/img
                COMMENT "Copying file ${img} to ${TGT}/html/img...")
        ENDFOREACH()

        # Convert PDF files and copy across
        FILE(GLOB_RECURSE pdffiles "img/*.pdf" "*/img/*.pdf"
            "${TUTORIAL_ROOT}/shared/img/*.pdf")
        FIND_PROGRAM(CONVERT convert)
        MARK_AS_ADVANCED(CONVERT)
        FOREACH(pdf ${pdffiles})
            GET_FILENAME_COMPONENT(BASENAME ${pdf} NAME_WE)
            ADD_CUSTOM_COMMAND(TARGET ${NEK_TARGET}-html POST_BUILD
                COMMAND ${CONVERT} ${pdf} ${TGT}/html/img/${BASENAME}.png
                COMMENT "Converting ${pdf} to PNG...")
        ENDFOREACH()

        # Store a 'clean' version for installation purposes.
        ADD_CUSTOM_COMMAND(TARGET ${NEK_TARGET}-html POST_BUILD
            COMMAND cmake -E copy_directory ${TGT}/html ${TGT}/html-only
            COMMENT "Making html-only copy without archive")

        # Install resulting files if generated.
        INSTALL(CODE "IF (EXISTS ${TGT}/html-only)
                FILE(INSTALL ${TGT}/html-only/
                DESTINATION \${CMAKE_INSTALL_PREFIX}/${NEKTAR_DOC_DIR}/tutorials/${NEK_TARGET}/html)
             ENDIF()")

        IF (NEK_ARCHIVE)
            SET(TARFILE "${TGT}/html/${NEK_TARGET}.tar.gz")
            ADD_CUSTOM_COMMAND(TARGET ${NEK_TARGET}-html POST_BUILD
                COMMAND ${CMAKE_COMMAND} -E tar "cvfz" ${TARFILE}
                    ${NEK_ARCHIVE}
                WORKING_DIRECTORY ${SRC}
                COMMENT "Generating ${TARFILE}")
            FOREACH(f ${NEK_ARCHIVE})
                GET_FILENAME_COMPONENT(TGTNAME ${f} NAME)
                ADD_CUSTOM_COMMAND(TARGET ${NEK_TARGET}-html POST_BUILD
                    COMMAND ${CMAKE_COMMAND} -E copy_directory ${f}
                        ${TGT}/html/${TGTNAME}
                    WORKING_DIRECTORY ${SRC}
                    COMMENT "Copying file ${f} to ${TGT}/html/${TGTNAME}...")
            ENDFOREACH()
        ENDIF()

        ADD_DEPENDENCIES(tutorials-html ${NEK_TARGET}-html)
    ENDIF()

    # Install tutorial files.
    FOREACH(f ${NEK_ARCHIVE})
        IF (IS_DIRECTORY ${SRC}/${f})
            INSTALL(DIRECTORY ${SRC}/${f}
                    DESTINATION ${NEKTAR_DOC_DIR}/tutorials/${NEK_TARGET})
        ELSEIF (EXISTS ${SRC}/${f})
            INSTALL(FILES ${SRC}/${f}
                    DESTINATION ${NEKTAR_DOC_DIR}/tutorials/${NEK_TARGET})
        ENDIF()
    ENDFOREACH()
ENDMACRO()

MACRO(ADD_NEKTAR_TUTORIAL_TEST solver testname)
    GET_FILENAME_COMPONENT(dir ${CMAKE_CURRENT_SOURCE_DIR} NAME)
    IF (TARGET ${solver})
        ADD_TEST(NAME tutorial_${testname}
            COMMAND $<TARGET_FILE:Tester> -e $<TARGET_FILE:${solver}>
            ${CMAKE_CURRENT_SOURCE_DIR}/tests/${testname}.tst)
    ELSE()
        MESSAGE(STATUS "Executable ${solver} is not being built. The tutorial "
                       "test, ${testname}, will be skipped.")
    ENDIF()
ENDMACRO()

MACRO(ADD_NEKPY_TUTORIAL_TEST testname)
    ADD_TEST(NAME tutorial_${testname}
        COMMAND $<TARGET_FILE:Tester>
        ${CMAKE_CURRENT_SOURCE_DIR}/tests/${testname}.tst)
ENDMACRO()

ADD_SUBDIRECTORY(basics)
#ADD_SUBDIRECTORY(events)
ADD_SUBDIRECTORY(fundamentals)
ADD_SUBDIRECTORY(incns)
ADD_SUBDIRECTORY(flow-stability)
ADD_SUBDIRECTORY(mesh-generation)
ADD_SUBDIRECTORY(cfs)
