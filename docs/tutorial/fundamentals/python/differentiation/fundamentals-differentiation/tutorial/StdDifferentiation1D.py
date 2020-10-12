#!/usr/bin/env python

from NekPy.LibUtilities import PointsKey, Points, PointsType
import numpy as np


def main():
    print("======================================================")
    print("|      DIFFERENTIATION IN A 1D STANDARD REGION       |")
    print("======================================================")
    print("Differentiate the function f(xi) = xi^7 in the ")
    print("standard segment xi=[-1,1] using quadrature points")

    # Specify the number of quadrature points
    nQuadPoints = 7

    # Calculate the quadrature zeros and the differentiation matrix.
    # This is done in 2 steps. Step 1: Declare a PointsKey which
    # uniquely defines the quadrature points (note that the type of
    # quadrature points is specified here).
    ptsKey = PointsKey(nQuadPoints, PointsType.GaussGaussLegendre)

    # Step 2: Using the PointsKey the points can be now created and
    # the quadrature zeros and the differentiation matrix can be
    # retrieved.
    pts = Points.Create(ptsKey)
    quadZeros = pts.GetZ()
    derivMatrix = pts.GetD()

    # Now that you have the quadrature zeros and the differentiation
    # matrix, apply the Gaussian quadrature technique to differentiate
    # the function f(xi) = xi^7 in the standard segment xi=[-1,1].
    # To do so, write a loop which performs the summation for each
    # quadrature point.

    # In Python, a loop is implemented as:
    # for i in range(min, max):
    #    # do something
    #
    # The function f(xi) can be evaluated using the command
    # 'pow(xi, 7)' of Python standard library
    #
    # Store the solution in the variable 'quadDerivs'

    quadDerivs = [0] * nQuadPoints

    # ==> Write your code here <==

    # Compute the total error
    error = 0
    for i in range(0, nQuadPoints):
        error += abs(quadDerivs[i] - 7 * pow(quadZeros[i], 6))

    # Display the output
    print("\t Q = %d: Error = %.6g" % (nQuadPoints, error))

    # Now evaluate the derivatives for a quadrature order of Q = Q_max
    # where Q_max is the number of quadrature points required for an
    # exact evaluation of the derivative (calculate this value
    # analytically).  Check that the error should then be zero (up to
    # numerical precision).


if __name__ == '__main__':
    main()
