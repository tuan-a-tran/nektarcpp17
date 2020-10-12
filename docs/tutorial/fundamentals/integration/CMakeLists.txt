ADD_NEKTAR_TUTORIAL(PDF HTML TARGET fundamentals-integration
    HTML_BREAK_LEVEL 2
    BASE fundamentals-integration
    STYLING_FILE styling.cfg
    ARCHIVE fundamentals-integration)

IF (NEKTAR_BUILD_LIBRARY)
    ADD_NEKTAR_EXECUTABLE(
        StdIntegration1D COMPONENT tutorial
        SOURCES fundamentals-integration/completed/StdIntegration1D.cpp
        DEPENDS StdRegions)
    ADD_NEKTAR_EXECUTABLE(
        StdIntegration2D COMPONENT tutorial
        SOURCES fundamentals-integration/completed/StdIntegration2D.cpp
        DEPENDS StdRegions)
    ADD_NEKTAR_EXECUTABLE(
        LocIntegration2D COMPONENT tutorial
        SOURCES fundamentals-integration/completed/LocIntegration2D.cpp
        DEPENDS StdRegions)
ENDIF()

# Add tests only if we are building from within the Nektar++ tree
IF (NEKTAR_BUILD_TESTS)
   ADD_NEKTAR_TUTORIAL_TEST(StdIntegration1D fundamentals-integration-std1D)
   ADD_NEKTAR_TUTORIAL_TEST(StdIntegration2D fundamentals-integration-std2D)
   ADD_NEKTAR_TUTORIAL_TEST(LocIntegration2D fundamentals-integration-loc2D)
ENDIF()
