#!/usr/bin/env python

from NekPy.LibUtilities import PointsKey, Points, PointsType


def main():
    print("===========================================================")
    print("|    INTEGRATION ON 2D ELEMENT in Standard Region         |")
    print("===========================================================")
    print("\n")
    print("Integrate the function f(x1,x2) = (x1)^12*(x2)^14")
    print("on the standard quadrilateral element:")

    # Specify the number of quadrature points in both directions
    nQuadPointsDir1 = 6
    nQuadPointsDir2 = 7

    # Calculate the quadrature zeros and weights in both directions.
    # This is done in 2 steps. Step 1: Declare a PointsKey which
    # uniquely defines the quadrature points (note that the type of
    # quadrature points is specified here).
    ptsKeyDir1 = PointsKey(nQuadPointsDir1, PointsType.GaussLobattoLegendre)
    ptsKeyDir2 = PointsKey(nQuadPointsDir2, PointsType.GaussLobattoLegendre)

    # Step 2: Using the PointsKey the points can be now created and
    # the quadrature zeros ad weights can be retrieved.
    ptsDir1 = Points.Create(ptsKeyDir1)
    ptsDir2 = Points.Create(ptsKeyDir2)
    quadZerosDir1, quadWeightsDir1 = ptsDir1.GetZW()
    quadZerosDir2, quadWeightsDir2 = ptsDir2.GetZW()

    # Now that you have the quadrature zeros and weights, apply the
    # Gaussian quadrature technique to integrate the function
    # f(x_1,i,x_2,j) = x_1,i^12 * x2,j^14 on the standard
    # quadrilateral. To do so, write a (double) loop which performs
    # the summation.
    #
    # Store the solution in the variable 'result'

    result = 0

    # ==> Write your code here <==

    # Display the output
    exactResult = 4.0/195.0
    print("\t q1 = %d  q2 = %d: Error = %.6g" % (
        nQuadPointsDir1, nQuadPointsDir2, abs(result - exactResult)))


if __name__ == '__main__':
    main()
