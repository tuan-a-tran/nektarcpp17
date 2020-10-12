ADD_NEKTAR_TUTORIAL(PDF HTML TARGET 2011-Cambridge-AIM BASE CambridgeTutorial
    STYLING_FILE styling.cfg HTML_BREAK_LEVEL 2)

# Add tests only if we are building from within the Nektar++ tree
IF (NEKTAR_BUILD_TESTS)
ENDIF()
