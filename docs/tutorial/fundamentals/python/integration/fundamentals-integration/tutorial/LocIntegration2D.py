#!/usr/bin/env python

from NekPy.LibUtilities import PointsKey, Points, PointsType


def main():
    print("===========================================================")
    print("|      INTEGRATION ON 2D ELEMENT in Local Region          |")
    print("===========================================================")
    print("\n")
    print("Integrate the function f(x1,x2) = x1^12 * x2^14 ")
    print("on a local quadrilateral element:")

    # Specify the number of quadrature points
    nQuadPointsDir1 = 6
    nQuadPointsDir2 = 7

    # Calculate the quadrature zeros and weights. This is done in 2
    # steps. Step 1: Declare a PointsKey which uniquely defines the
    # quadrature points (note that the type of quadrature points is
    # specified here).
    ptsKeyDir1 = PointsKey(nQuadPointsDir1, PointsType.GaussLobattoLegendre)
    ptsKeyDir2 = PointsKey(nQuadPointsDir2, PointsType.GaussLobattoLegendre)

    # Step 2: Using the PointsKey the points can be now created and
    # the quadrature zeros ad weights can be retrieved.
    ptsDir1 = Points.Create(ptsKeyDir1)
    ptsDir2 = Points.Create(ptsKeyDir2)
    z1, w1 = ptsDir1.GetZW()
    z2, w2 = ptsDir2.GetZW()

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

    # Integrate the function f(x1,x2) = x1^12 * x2^14 on a local
    # quadrilateral element (defined above). Use 7th order
    # Gauss-Lobatto-Legendre quadrature in both directions.
    #
    # Your code can be based on the previous exercise. However,
    # as we are calculating the integral of a function defined on
    # a local element rather than on a reference element, we have
    # to take into accoun the geometry of the element.
    #
    # Therefore, the implementation should be altered in two ways:
    # (1) The quadrature zeros should be transformed to local
    #     coordinates to evaluate the integrand f(x1,x2)
    # (2) Take into account the Jacobian of the transformation
    #     between local and reference coordinates when evaluating
    #     the integral. (Evaluate the expression for the Jacobian
    #     analytically rather than using numerical
    #     differentiation)

    # Store the solution in the variable 'result'
    result = 0.0

    # Apply the Gaussian quadrature technique to integrate the
    # function f(x1,x2) = x1^12 * x2^14 on the standard
    # quadrilateral.  To do so, edit the (double) loop which performs
    # the summation.

    for i in range(0, nQuadPointsDir1):
        for j in range(0, nQuadPointsDir2):

            # Calculate the local coordinates of the quadrature zeros
            # using the mapping from reference to local element
            x1 = x1_A * 0.25 * (1 - z1[i]) * (1 - z2[j]) + \
                 x1_B * 0.25 * (1 + z1[i]) * (1 - z2[j]) + \
                 x1_D * 0.25 * (1 - z1[i]) * (1 + z2[j]) + \
                 x1_C * 0.25 * (1 + z1[i]) * (1 + z2[j])

            x2 = x2_A * 0.25 * (1 - z1[i]) * (1 - z2[j]) + \
                 x2_B * 0.25 * (1 + z1[i]) * (1 - z2[j]) + \
                 x2_D * 0.25 * (1 - z1[i]) * (1 + z2[j]) + \
                 x2_C * 0.25 * (1 + z1[i]) * (1 + z2[j])

            # Analytically evaluate the Jacobian

            # ==> Write your code here <==
            jacobian =

            result += pow(x1, 12) * pow(x2, 14) * w1[i] * w2[j] * abs(jacobian)

    # Display the output
    exactResult = 1.0/195.0 + 1.0/420.0
    print("\t Error = %.6g" % (abs(result - exactResult)))


if __name__ == '__main__':
    main()
