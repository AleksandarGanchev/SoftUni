from unittest import TestCase, main
# from worker import Worker


class TestWorker(TestCase):
    def setUp(self):
        self.worker = Worker("DonaldTrump", 60000, 100)

    def test_correct_innit(self):
        self.assertEqual("DonaldTrump", self.worker.name)
        self.assertEqual(60000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_when_worker_has_energy_if_salary_is_increased_and_energy_is_decreased(self):
        expected_money = self.worker.salary
        expected_energy = self.worker.energy - 1

        self.worker.work()

        self.assertEqual(expected_money, self.worker.money)
        self.assertEqual(expected_energy, self.worker.energy)

    def test_check_if_exception_is_raised_when_energy_is_zero_or_below_zero(self):
        self.worker.energy = -10
        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_if_energy_is_increased_when_worker_rest(self):
        expected_energy = self.worker.energy + 1
        self.worker.rest()

        self.assertEqual(expected_energy, self.worker.energy)

    def test_if_get_info_return_the_correct_information(self):
        self.assertEqual(f"DonaldTrump has saved 0 money.", self.worker.get_info())


if __name__ == "__main__":
    main()
