ADD_NEKTAR_TUTORIAL(PDF HTML TARGET basics-advection-diffusion
    HTML_BREAK_LEVEL 2
    BASE basics-advection-diffusion
    STYLING_FILE styling.cfg
    ARCHIVE basics-advection-diffusion)

# Add tests only if we are building from within the Nektar++ tree
IF (NEKTAR_BUILD_TESTS)
    IF(NEKTAR_UTILITY_NEKMESH)
        ADD_NEKTAR_TUTORIAL_TEST(NekMesh      basics-advection-diffusion-msh)
        ADD_NEKTAR_TUTORIAL_TEST(NekMesh      basics-advection-diffusion-msh-align)
    ENDIF()
    IF(NEKTAR_UTILITY_FIELDCOVERT)
        ADD_NEKTAR_TUTORIAL_TEST(FieldConvert basics-advection-diffusion-post)
    ENDIF()
    IF(NEKTAR_SOLVER_ADR)
        ADD_NEKTAR_TUTORIAL_TEST(ADRSolver    basics-advection-diffusion-slv)
    ENDIF()
ENDIF()
