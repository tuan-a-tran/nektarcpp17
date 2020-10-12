#!/usr/bin/env python

from NekPy.LibUtilities import PointsKey, Points, PointsType


def main():
    print("======================================================")
    print("|        INTEGRATION ON A 1D STANDARD REGION         |")
    print("======================================================")

    print("Integrate the function f(xi) = xi^12 on the standard ")
    print("segment xi=[-1,1] with Gaussian quadrature")

    # Specify the number of quadrature points
    nQuadPoints = 4

    # Calculate the quadrature zeros and weights. This is done in 2
    # steps. Step 1: Declare a PointsKey which uniquely defines the
    # quadrature points (note that the type of quadrature points is
    # specified here).
    ptsKey = PointsKey(nQuadPoints, PointsType.GaussGaussLegendre)

    # Step 2: Using the PointsKey the points can be now created and
    # the quadrature zeros and weights can be retrieved.
    pts = Points.Create(ptsKey)
    quadZeros, quadWeights = pts.GetZW()

    # Now that you have the quadrature zeros and weight, apply the
    # Gaussian quadrature technique to integrate the function
    # f(xi) = xi^12 on the standard segment xi=[-1,1]. To do so,
    # write a loop which performs the summation.
    #
    # In Python, a loop is implemented as:
    # for i in range(min, max):
    #    # do something
    #
    # The function f(xi) can be evaluated using the command
    # 'pow(xi, 12)' of Python standard library
    #
    # Store the solution in the variable 'result'

    result = 0
    for i in range(0, nQuadPoints):
        result += pow(quadZeros[i], 12) * quadWeights[i]

    # Display the output
    exactResult = 2.0/13.0
    print("\t Q = %d: Error = %.6g" % (nQuadPoints, abs(result - exactResult)))

    # Now evaluate the integral for a quadrature order of Q = Q_max
    # where Q_max is the number of quadrature points required for an
    # exact evaluation of the integral (calculate this value
    # analytically). Check that the error is then zero (up to numerical
    # precision).


if __name__ == '__main__':
    main()
