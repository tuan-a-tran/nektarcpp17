ADD_NEKTAR_TUTORIAL(PDF HTML TARGET fundamentals-differentiation-python
    HTML_BREAK_LEVEL 2
    BASE fundamentals-differentiation
    STYLING_FILE styling.cfg
    ARCHIVE fundamentals-differentiation)

ADD_NEKPY_EXECUTABLE(LocDifferentiation2D.py fundamentals-differentiation/completed/LocDifferentiation2D.py)
ADD_NEKPY_EXECUTABLE(StdDifferentiation1D.py fundamentals-differentiation/completed/StdDifferentiation1D.py)
ADD_NEKPY_EXECUTABLE(StdDifferentiation2D.py fundamentals-differentiation/completed/StdDifferentiation2D.py)

IF (NEKTAR_BUILD_TESTS)
   ADD_NEKPY_TUTORIAL_TEST(fundamentals-differentiation-std1D-python)
   ADD_NEKPY_TUTORIAL_TEST(fundamentals-differentiation-std2D-python)
   ADD_NEKPY_TUTORIAL_TEST(fundamentals-differentiation-loc2D-python)
ENDIF()
