ADD_NEKTAR_TUTORIAL(PDF HTML TARGET flow-stability-cylinder
    HTML_BREAK_LEVEL 2
    BASE flow-stability-cylinder
    STYLING_FILE styling.cfg
    ARCHIVE flow-stability-cylinder)

# Add tests only if we are building from within the Nektar++ tree
IF (NEKTAR_BUILD_TESTS)
    IF(NEKTAR_SOLVER_INCNAVIERSTOKES)
        ADD_NEKTAR_TUTORIAL_TEST(IncNavierStokesSolver flow-stability-cylinder-base)
        ADD_NEKTAR_TUTORIAL_TEST(IncNavierStokesSolver
            flow-stability-cylinder-direct)
            ADD_NEKTAR_TUTORIAL_TEST(IncNavierStokesSolver
            flow-stability-cylinder-adjoint)
    ENDIF()
ENDIF()
