ADD_NEKTAR_TUTORIAL(PDF HTML TARGET fundamentals-integration-python
    HTML_BREAK_LEVEL 2
    BASE fundamentals-integration
    STYLING_FILE styling.cfg
    ARCHIVE fundamentals-integration)

ADD_NEKPY_EXECUTABLE(LocIntegration2D.py fundamentals-integration/completed/LocIntegration2D.py)
ADD_NEKPY_EXECUTABLE(StdIntegration1D.py fundamentals-integration/completed/StdIntegration1D.py)
ADD_NEKPY_EXECUTABLE(StdIntegration2D.py fundamentals-integration/completed/StdIntegration2D.py)

IF (NEKTAR_BUILD_TESTS)
   ADD_NEKPY_TUTORIAL_TEST(fundamentals-integration-std1D-python)
   ADD_NEKPY_TUTORIAL_TEST(fundamentals-integration-std2D-python)
   ADD_NEKPY_TUTORIAL_TEST(fundamentals-integration-loc2D-python)
ENDIF()