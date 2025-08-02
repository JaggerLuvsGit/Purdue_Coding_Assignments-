import unittest
from log_analyzer import LogEntry  # Ensure this import matches your directory structure

class TestLogEntry(unittest.TestCase):

    def test_event_time_conversion(self):
        log = LogEntry('2022-01-01 08:29:25 UTC', '192.168.1.1', 80, 'TCP', 'Allow', 123, '216.57.223.121', 'US', 'United States')
        
        # Assert that the month is correct
        self.assertEqual(log.event_time.month, 1)
        # Assert that the hour is correct
        self.assertEqual(log.event_time.hour, 8)

    def test_ipv4_class(self):
        log_a = LogEntry('2022-01-01 00:18:38 UTC', '192.168.1.1', 80, 'TCP', 'Allow', 123, '11.177.69.220', 'US', 'United States')
        self.assertEqual(log_a.ipv4_class, "A")  # Should pass

        log_b = LogEntry('2022-01-01 00:18:38 UTC', '192.168.1.1', 80, 'TCP', 'Allow', 123, '173.205.219.112', 'US', 'United States')
        self.assertEqual(log_b.ipv4_class, "B")  # Should pass

        log_c = LogEntry('2022-01-01 00:18:38 UTC', '192.168.1.1', 80, 'TCP', 'Allow', 123, '229.163.4.51', 'US', 'United States')
        self.assertEqual(log_c.ipv4_class, "D")  # Should pass

        log_invalid = LogEntry('2022-01-01 00:18:38 UTC', '192.168.1.1', 80, 'TCP', 'Allow', 123, '300.163.4.51', 'US', 'United States')
        self.assertEqual(log_invalid.ipv4_class, "Unknown")  # Should pass

if __name__ == '__main__':
    unittest.main()