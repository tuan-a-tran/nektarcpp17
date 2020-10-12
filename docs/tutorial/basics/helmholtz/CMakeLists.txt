ADD_NEKTAR_TUTORIAL(PDF HTML TARGET basics-helmholtz
    HTML_BREAK_LEVEL 2
    BASE basics-helmholtz
    STYLING_FILE styling.cfg
    ARCHIVE basics-helmholtz)

# Add tests only if we are building from within the Nektar++ tree
IF (NEKTAR_BUILD_TESTS)
    IF(NEKTAR_UTILITY_NEKMESH)
        ADD_NEKTAR_TUTORIAL_TEST(NekMesh      basics-helmholtz-msh)
    ENDIF()
    IF(NEKTAR_UTILITY_FIELDCOVERT)
        ADD_NEKTAR_TUTORIAL_TEST(FieldConvert basics-helmholtz-post)
    ENDIF()
    IF(NEKTAR_SOLVER_ADR)
        ADD_NEKTAR_TUTORIAL_TEST(ADRSolver    basics-helmholtz-slv)
    ENDIF()
ENDIF()
