from unittest import TestCase, main
# from cat import Cat


class TestCat(TestCase):
    def setUp(self):
        self.cat = Cat("Felix")

    def test_correct_innit(self):
        self.assertEqual("Felix", self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_feed_cat_increase_size_and_cat_sleepy(self):
        expected_size = self.cat.size + 1
        self.cat.eat()

        self.assertEqual(expected_size, self.cat.size)
        self.assertTrue(self.cat.sleepy)
        self.assertTrue(self.cat.fed)

    def test_feed_cat_when_cat_have_already_been_fed_raise_exception(self):
        self.cat.fed = True
        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual('Already fed.', str(ex.exception))

    def test_make_hungry_cat_to_sleep_when_hungry_raise_exception(self):
        self.cat.fed = False
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_make_cat_sleep_when_cat_already_slept(self):
        self.cat.sleepy = True
        self.cat.fed = True

        self.cat.sleep()

        self.assertFalse(self.cat.sleepy)

if __name__ == "__main__":
    main()
