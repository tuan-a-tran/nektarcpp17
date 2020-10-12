ADD_NEKTAR_TUTORIAL(PDF HTML TARGET 2015-Imperial-NektarWorkshop
    BASE Imperial-NektarWorkshop USES_REFS
    STYLING_FILE styling.cfg)

# Add tests only if we are building from within the Nektar++ tree
IF (NEKTAR_BUILD_TESTS)
ENDIF()
