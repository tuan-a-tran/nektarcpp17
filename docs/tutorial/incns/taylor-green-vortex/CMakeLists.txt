ADD_NEKTAR_TUTORIAL(PDF HTML TARGET incns-taylor-green-vortex
    HTML_BREAK_LEVEL 2
    BASE incns-taylor-green-vortex
    STYLING_FILE styling.cfg
    ARCHIVE incns-taylor-green-vortex)

# Add tests only if we are building from within the Nektar++ tree
IF (NEKTAR_BUILD_TESTS)
    IF (NEKTAR_USE_MPI AND NEKTAR_USE_FFTW AND NEKTAR_SOLVER_INCNAVIERSTOKES)
        ADD_NEKTAR_TUTORIAL_TEST(IncNavierStokesSolver incns-taylor-green-vortex-64)
    ENDIF()
ENDIF()
