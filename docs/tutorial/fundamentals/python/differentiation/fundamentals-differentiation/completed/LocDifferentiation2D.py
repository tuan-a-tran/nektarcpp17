#!/usr/bin/env python

from NekPy.LibUtilities import PointsKey, Points, PointsType
import numpy as np


def main():
    print("=========================================================")
    print("|     DIFFERENTIATION IN 2D ELEMENT in Local Region     |")
    print("=========================================================")
    print("Differentiate the function f(x1,x2) = x1^7 * x2^9 ")
    print("in a local quadrilateral element:")

    # Specify the number of quadrature points in both directions
    nQuadPointsDir1 = 8
    nQuadPointsDir2 = 10

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

    # The local (straight-sided) quadrilateral element has the
    # following vertices:
    #
    # - Vertex A: (x1_A,x2_A) = (0,-1)
    # - Vertex B: (x1_A,x2_A) = (1,-1)
    # - Vertex C: (x1_A,x2_A) = (1,1)
    # - Vertex D: (x1_A,x2_A) = (0,0)

    x1_A = 0.0
    x2_A = -1.0

    x1_B = 1.0
    x2_B = -1.0

    x1_C = 1.0
    x2_C = 1.0

    x1_D = 0.0
    x2_D = 0.0

    # Differentiate the function f(x1,x2) = x1^7 * x2^9 in a local
    # quadrilateral element (defined above). Use Gauss-Lobatto-Legendre
    # quadrature in both directions.
    #
    # Your code can be based on the previous exercise. However
    # as we are calculating the derivatives of a function defined in
    # a local element rather than in a reference element, we have
    # to take into account the geometry of the element.
    #
    # Therefore, the implementation should be altered in two ways:
    #
    # (1) The quadrature zeros should be transformed to local
    #     coordinates to evaluate the function f(x1,x2)
    #
    # (2) Take into account the Jacobian matrix of the transformation
    #     between local and reference coordinates when evaluating
    #     the derivative. (Evaluate the expression for the Jacobian
    #     matrix analytically rather than using numerical
    #     differentiation and invert it)
    #
    # Store the solution in the matrices 'quadDerivsDir1' and 'quadDerivsDir2'

    quadDerivsDir1 = np.zeros((nQuadPointsDir1, nQuadPointsDir2))
    quadDerivsDir2 = np.zeros((nQuadPointsDir1, nQuadPointsDir2))

    # Apply the Gaussian quadrature technique to differentiate the
    # function f(x1,x2) = x1^7 * x2^9 in the standard
    # quadrilateral.  To do so, edit the (double) loop which performs
    # the summation.

    error = 0

    for i in range(0, nQuadPointsDir1):
        for j in range(0, nQuadPointsDir2):
            # Compute the local coordinates of the quadrature point
            x1_master = (
                x1_A * 0.25 * (1 - quadZerosDir1[i]) * (1 - quadZerosDir2[j])
                + x1_B * 0.25 * (1 + quadZerosDir1[i]) * (1 - quadZerosDir2[j])
                + x1_D * 0.25 * (1 - quadZerosDir1[i]) * (1 + quadZerosDir2[j])
                + x1_C * 0.25 * (1 + quadZerosDir1[i]) * (1 + quadZerosDir2[j])
                )
            x2_master = (
                x2_A * 0.25 * (1 - quadZerosDir1[i]) * (1 - quadZerosDir2[j])
                + x2_B * 0.25 * (1 + quadZerosDir1[i]) * (1 - quadZerosDir2[j])
                + x2_D * 0.25 * (1 - quadZerosDir1[i]) * (1 + quadZerosDir2[j])
                + x2_C * 0.25 * (1 + quadZerosDir1[i]) * (1 + quadZerosDir2[j])
                )

            # Fill the Jacobian matrix analytically with the dx?dxi? terms
            dx1dxi1 = (
                      0.25 * (1 - quadZerosDir2[j]) * (x1_B - x1_A) +
                      0.25 * (1 + quadZerosDir2[j]) * (x1_C - x1_D)
                      )
            dx2dxi2 = (
                      0.25 * (1 - quadZerosDir1[i]) * (x2_D - x2_A) +
                      0.25 * (1 + quadZerosDir1[i]) * (x2_C - x2_B)
                      )
            dx1dxi2 = (
                      0.25 * (1 - quadZerosDir1[i]) * (x1_D - x1_A) +
                      0.25 * (1 + quadZerosDir1[i]) * (x1_C - x1_B)
                      )
            dx2dxi1 = (
                      0.25 * (1 - quadZerosDir2[j]) * (x2_B - x2_A) +
                      0.25 * (1 + quadZerosDir2[j]) * (x2_C - x2_D)
                      )

            # Compute the Jacobian determinant
            jacobian = dx1dxi1 * dx2dxi2 - dx1dxi2 * dx2dxi1

            # Invert the Jacobian matrix to obtain the dx?dxi? terms
            dxi1dx1 = dx2dxi2 / jacobian
            dxi2dx2 = dx1dxi1 / jacobian
            dxi1dx2 = -dx1dxi2 / jacobian
            dxi2dx1 = -dx2dxi1 / jacobian

            for k in range(0, nQuadPointsDir1):
                # Compute the local coordinates of the quadrature point
                x1_slave = (
                    x1_A * 0.25 * (1 - quadZerosDir1[k])
                    * (1 - quadZerosDir2[j])
                    + x1_B * 0.25 * (1 + quadZerosDir1[k])
                    * (1 - quadZerosDir2[j])
                    + x1_D * 0.25 * (1 - quadZerosDir1[k])
                    * (1 + quadZerosDir2[j])
                    + x1_C * 0.25 * (1 + quadZerosDir1[k])
                    * (1 + quadZerosDir2[j])
                    )
                x2_slave = (
                    x2_A * 0.25 * (1 - quadZerosDir1[k])
                    * (1 - quadZerosDir2[j])
                    + x2_B * 0.25 * (1 + quadZerosDir1[k])
                    * (1 - quadZerosDir2[j])
                    + x2_D * 0.25 * (1 - quadZerosDir1[k])
                    * (1 + quadZerosDir2[j])
                    + x2_C * 0.25 * (1 + quadZerosDir1[k])
                    * (1 + quadZerosDir2[j])
                    )

                # Add the contribution of this quadrature point to
                # quadDerivsDir1[i][j] and quadDerivsDir2[i][j]
                quadDerivsDir1[i][j] += (
                                        derivMatrixDir1[i][k]
                                        * pow(x1_slave, 7)
                                        * pow(x2_slave, 9) * dxi1dx1
                                        )
                quadDerivsDir2[i][j] += (
                                        derivMatrixDir1[i][k]
                                        * pow(x1_slave, 7)
                                        * pow(x2_slave, 9) * dxi1dx2
                                        )

            for k in range(0, nQuadPointsDir2):
                # Compute the local coordinates of the quadrature point
                x1_slave = (
                    x1_A * 0.25 * (1 - quadZerosDir1[i])
                    * (1 - quadZerosDir2[k])
                    + x1_B * 0.25 * (1 + quadZerosDir1[i])
                    * (1 - quadZerosDir2[k])
                    + x1_D * 0.25 * (1 - quadZerosDir1[i])
                    * (1 + quadZerosDir2[k])
                    + x1_C * 0.25 * (1 + quadZerosDir1[i])
                    * (1 + quadZerosDir2[k])
                    )
                x2_slave = (
                    x2_A * 0.25 * (1 - quadZerosDir1[i])
                    * (1 - quadZerosDir2[k])
                    + x2_B * 0.25 * (1 + quadZerosDir1[i])
                    * (1 - quadZerosDir2[k])
                    + x2_D * 0.25 * (1 - quadZerosDir1[i])
                    * (1 + quadZerosDir2[k])
                    + x2_C * 0.25 * (1 + quadZerosDir1[i])
                    * (1 + quadZerosDir2[k])
                    )

                # Add the contribution of this quadrature point to
                # quadDerivsDir1[i][j] and quadDerivsDir2[i][j]
                quadDerivsDir2[i][j] += (
                                        derivMatrixDir2[j][k]
                                        * pow(x1_slave, 7)
                                        * pow(x2_slave, 9) * dxi2dx2
                                        )
                quadDerivsDir1[i][j] += (
                                        derivMatrixDir2[j][k]
                                        * pow(x1_slave, 7)
                                        * pow(x2_slave, 9) * dxi2dx1
                                        )

            error += abs(quadDerivsDir1[i][j] -
                         7 * pow(x1_master, 6) * pow(x2_master, 9))
            error += abs(quadDerivsDir2[i][j] -
                         9 * pow(x1_master, 7) * pow(x2_master, 8))

    # Display the average error
    avg_error = error / (nQuadPointsDir1 * nQuadPointsDir2)
    print("\t q1 = %d, q2 = %d: Average Error = %.6g" % (nQuadPointsDir1,
                                                         nQuadPointsDir2,
                                                         avg_error))


if __name__ == '__main__':
    main()
