#!/usr/bin/env python

from NekPy.LibUtilities import PointsKey, Points, PointsType
import numpy as np


def main():
    print("========================================================")
    print("|   DIFFERENTIATION IN 2D ELEMENT in Standard Region   |")
    print("========================================================")
    print("Differentiate the function f(x1,x2) = (x1)^7*(x2)^9")
    print("in the standard quadrilateral element:")

    # Specify the number of quadrature points in both directions
    nQuadPointsDir1 = 7
    nQuadPointsDir2 = 9

    # Calculate the quadrature zeros and the differentiation matrix
    # in both directions. This is done in 2 steps. Step 1: Declare
    # a PointsKey which uniquely defines the quadrature points (note
    # that the type of quadrature points is specified here).
    ptsKeyDir1 = PointsKey(nQuadPointsDir1, PointsType.GaussLobattoLegendre)
    ptsKeyDir2 = PointsKey(nQuadPointsDir2, PointsType.GaussLobattoLegendre)

    # Step 2: Using the PointsKey the points can be now created and
    # the quadrature zeros and the differentiation matrix can be
    # retrieved.
    ptsDir1 = Points.Create(ptsKeyDir1)
    ptsDir2 = Points.Create(ptsKeyDir2)

    quadZerosDir1 = ptsDir1.GetZ()
    quadZerosDir2 = ptsDir2.GetZ()

    derivMatrixDir1 = ptsDir1.GetD()
    derivMatrixDir2 = ptsDir2.GetD()

    # Now you have the quadrature zeros and the differentiation matrix,
    # apply the Gaussian quadrature technique to differentiate the function
    # f(x_1,i,x_2,j) = x_1,i^7 * x2,j^9 on the standard
    # quadrilateral.  To do so, write a (triple) loop which performs
    # the summation.
    #
    # Store the solution in the numpy matrices 'quadDerivsDir1' and
    # 'quadDerivsDir2'
    quadDerivsDir1 = np.zeros((nQuadPointsDir1, nQuadPointsDir2))
    quadDerivsDir2 = np.zeros((nQuadPointsDir1, nQuadPointsDir2))

    for i in range(0, nQuadPointsDir1):
        for j in range(0, nQuadPointsDir2):
            for k in range(0, nQuadPointsDir1):
                quadDerivsDir1[i][j] += derivMatrixDir1[i][k] * \
                                        pow(quadZerosDir1[k], 7) * \
                                        pow(quadZerosDir2[j], 9)
            for k in range(0, nQuadPointsDir2):
                quadDerivsDir2[i][j] += derivMatrixDir2[j][k] * \
                                        pow(quadZerosDir1[i], 7) * \
                                        pow(quadZerosDir2[k], 9)

    # Compute the total error
    error = 0
    for i in range(0, nQuadPointsDir1):
        for j in range(0, nQuadPointsDir2):
            error += abs(quadDerivsDir1[i][j] - 7 *
                         pow(quadZerosDir1[i], 6) *
                         pow(quadZerosDir2[j], 9))
            error += abs(quadDerivsDir2[i][j] - 9 *
                         pow(quadZerosDir1[i], 7) *
                         pow(quadZerosDir2[j], 8))

    # Display the output
    print("\t q1 = %d, q2 = %d: Error = %.6g" % (nQuadPointsDir1,
                                                 nQuadPointsDir2,
                                                 error))


if __name__ == '__main__':
    main()
