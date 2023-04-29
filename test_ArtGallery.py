import unittest
from RefactoredArtGallery import *

class TestArtGalleryMethods(unittest.TestCase):

    def setUp(self):
        self.vertex1 = Point(2, 3)
        self.vertex2 = Point(4, 5)

        self.polygon = [Point(0, 0), Point(5, 0), Point(5, 5), Point(0, 5)]
        self.triangleList = triangulatePolygon(self.polygon)

    def test_crossProduct(self):
        self.assertEqual(crossProduct(self.vertex1, self.vertex2), -2)

    def test_polygonArea(self):

        posWinding = [Point(0,0), Point(0,1), Point(1,1), Point(1,0)]
        negWinding = [Point(0,0), Point(1,0), Point(1,1), Point(0,1)]

        self.assertGreaterEqual(polygonArea(posWinding), 0)
        self.assertLessEqual(polygonArea(negWinding), 0)

    def test_getCircularIndex(self):
        listLength3 = [0, 1, 2]
        self.assertEqual(getCircularIndex(listLength3, 0), 0)
        self.assertEqual(getCircularIndex(listLength3, -1), 2)
        self.assertEqual(getCircularIndex(listLength3, 5), 2)

    def test_isPointInsideTriangle(self):
        triPointA = Point(0, 0)
        triPointB = Point(0, 4)
        triPointC = Point(4, 0)
        pointInside = Point(0.5, 0.5)
        pointOutside = Point(5, 5)

        self.assertTrue(isPointInsideTriangle(pointInside, triPointA, triPointB, triPointC))
        self.assertFalse(isPointInsideTriangle(pointOutside, triPointA, triPointB, triPointC))

    def test_returnIndexSmallestInt(self):
        mylist = [2, 3, 4, 1, 10]
        self.assertEqual(returnIndexSmallestInt(mylist), 3)

    def test_isOdd(self):
        self.assertTrue(isOdd(3))
        self.assertFalse(isOdd(4))

    def test_colorVerticies(self):
        self.assertEqual(colorVerticies(self.triangleList), [1, 2, 1, 3])

    def test_triangulatePolygon(self):
        posWindingOrderPolygon = [Point(0, 0), Point(0, 5), Point(5, 5), Point(5, 0)]
        negWindingOrderPolygon = [Point(0, 0), Point(5, 0), Point(5, 5), Point(0, 5)]
        incompletePolygon = [Point(0, 0), Point(0, 1)]

        self.assertEqual(triangulatePolygon(incompletePolygon), 1)
        self.assertEqual(triangulatePolygon(posWindingOrderPolygon), [[3, 0, 1], [1, 2, 3]])
        self.assertEqual(triangulatePolygon(negWindingOrderPolygon), [[3, 0, 1], [1, 2, 3]])




    
