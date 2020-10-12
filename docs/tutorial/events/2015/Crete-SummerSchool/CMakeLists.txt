ADD_NEKTAR_TUTORIAL(PDF HTML TARGET 2015-Crete-SummerSchool BASE CreteTutorial
    STYLING_FILE styling.cfg)

# Add tests only if we are building from within the Nektar++ tree
IF (NEKTAR_BUILD_TESTS)
ENDIF()
