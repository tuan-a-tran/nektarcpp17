ADD_NEKTAR_TUTORIAL(PDF HTML TARGET fundamentals-differentiation
    HTML_BREAK_LEVEL 2
    BASE fundamentals-differentiation
    STYLING_FILE styling.cfg
    ARCHIVE fundamentals-differentiation)

#ADD_NEKTAR_EXECUTABLE(
#    StdDifferentiation1D COMPONENT tutorial
#    SOURCES fundamentals-differentiation/completed/StdDifferentiation1D.cpp
#    DEPENDS StdRegions)
#ADD_NEKTAR_EXECUTABLE(
#    StdDifferentiation2D COMPONENT tutorial
#    SOURCES fundamentals-differentiation/completed/StdDifferentiation2D.cpp
#    DEPENDS StdRegions)
#ADD_NEKTAR_EXECUTABLE(
#    LocDifferentiation2D COMPONENT tutorial
#    SOURCES fundamentals-differentiation/completed/LocDifferentiation2D.cpp
#    DEPENDS StdRegions)

# Add tests only if we are building from within the Nektar++ tree
IF (NEKTAR_BUILD_TESTS)
   ADD_NEKTAR_TUTORIAL_TEST(StdDifferentiation1D fundamentals-differentiation-std1D)
   ADD_NEKTAR_TUTORIAL_TEST(StdDifferentiation2D fundamentals-differentiation-std2D)
   ADD_NEKTAR_TUTORIAL_TEST(LocDifferentiation2D fundamentals-differentiation-loc2D)
ENDIF()
