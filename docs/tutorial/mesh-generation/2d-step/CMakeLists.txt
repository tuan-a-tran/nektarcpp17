ADD_NEKTAR_TUTORIAL(PDF HTML TARGET mesh-generation-2d-step
    HTML_BREAK_LEVEL 2
    BASE mesh-generation-2d-step
    STYLING_FILE styling.cfg
    ARCHIVE mesh-generation-2d-step)

IF (NEKTAR_USE_MESHGEN)
    IF(NEKTAR_BUILD_TESTS)
        ADD_NEKTAR_TUTORIAL_TEST(NekMesh mesh-generation-2d-step)
    ENDIF()
ENDIF()
