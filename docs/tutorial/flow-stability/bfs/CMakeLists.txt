ADD_NEKTAR_TUTORIAL(PDF HTML TARGET flow-stability-bfs
    HTML_BREAK_LEVEL 2
    BASE flow-stability-bfs
    STYLING_FILE styling.cfg
    ARCHIVE flow-stability-bfs)

# Add tests only if we are building from within the Nektar++ tree
IF (NEKTAR_BUILD_TESTS)
    IF(NEKTAR_SOLVER_INCNAVIERSTOKES)
        ADD_NEKTAR_TUTORIAL_TEST(IncNavierStokesSolver flow-stability-bfs-base)
        ADD_NEKTAR_TUTORIAL_TEST(IncNavierStokesSolver flow-stability-bfs-tg)
    ENDIF()
ENDIF()
