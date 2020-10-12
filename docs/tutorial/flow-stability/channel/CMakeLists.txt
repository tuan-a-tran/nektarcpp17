ADD_NEKTAR_TUTORIAL(PDF HTML TARGET flow-stability-channel
    HTML_BREAK_LEVEL 2
    BASE flow-stability-channel
    STYLING_FILE styling.cfg
    ARCHIVE flow-stability-channel)

# Add tests only if we are building from within the Nektar++ tree
IF (NEKTAR_BUILD_TESTS)
    IF(NEKTAR_SOLVER_INCNAVIERSTOKES)
        ADD_NEKTAR_TUTORIAL_TEST(IncNavierStokesSolver flow-stability-channel-base)
        ADD_NEKTAR_TUTORIAL_TEST(IncNavierStokesSolver flow-stability-channel-vcs)
        ADD_NEKTAR_TUTORIAL_TEST(IncNavierStokesSolver
            flow-stability-channel-coupled)
    ENDIF()
ENDIF()
