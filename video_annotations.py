#!/usr/bin/env python
# md5: 1380e7c85a2cb8adf14609d9c7b2f494
# coding: utf-8

def timeToSeconds(timestr):
  minutes,seconds = tuple(timestr.split(':'))
  minutes = int(minutes)
  seconds = int(seconds)
  return minutes*60 + seconds

class TRange:
  def __init__(self, start, end):
    if type(start) == type(''):
      start = timeToSeconds(start)
    if type(end) == type(''):
      end = timeToSeconds(end)
    self.start = start
    self.end = end

video_lengths_ml_004_human_readable = {
  1: "6:54",
  2: "7:14",
  3: "12:29",
  4: "14:13",
  5: "8:10",
  6: "8:12",
  7: "11:09",
  8: "8:48",
  11: "11:30",
  10: "11:50",
  9: "10:20",
  12: "5:49",
  13: "8:45",
  14: "6:53",
  15: "13:39",
  16: "11:09",
  17: "9:02",
  18: "11:12",
  19: "8:22",
  20: "5:04",
  21: "8:51",
  22: "8:58",
  23: "7:39",
  24: "16:17",
  25: "5:58",
  26: "13:59",
  27: "16:07",
  28: "13:14",
  29: "9:38",
  31: "12:55",
  30: "13:48",
  32: "3:33",
  33: "8:08",
  34: "7:24",
  35: "14:49",
  58: "11:25",
  36: "10:14",
  37: "14:06",
  38: "6:15",
  39: "9:42",
  40: "10:10",
  41: "10:40",
  42: "8:33",
  43: "9:35",
  44: "7:47",
  45: "12:01",
  46: "11:46",
  47: "7:15",
  48: "10:20",
  49: "3:51",
  50: "6:43",
  51: "11:59",
  52: "12:44",
  53: "7:47",
  54: "11:37",
  55: "6:51",
  56: "13:23",
  57: "6:30",
  59: "5:50",
  60: "7:35",
  61: "12:03",
  62: "7:42",
  63: "11:20",
  64: "11:53",
  65: "6:50",
  66: "9:29",
  67: "13:11",
  68: "11:35",
  69: "14:05",
  70: "11:09",
  71: "14:47",
  72: "10:36",
  73: "19:41",
  74: "15:44",
  75: "15:43",
  76: "21:02",
  77: "3:16",
  78: "12:32",
  79: "7:04",
  80: "7:49",
  81: "8:22",
  82: "10:09",
  83: "5:27",
  84: "9:05",
  85: "15:13",
  86: "10:30",
  87: "3:54",
  88: "12:48",
  89: "7:38",
  90: "10:27",
  91: "12:02",
  92: "13:07",
  93: "7:36",
  95: "12:17",
  96: "13:45",
  97: "14:03",
  98: "7:54",
  99: "14:31",
  100: "10:14",
  101: "8:26",
  102: "8:27",
  103: "8:30",
  104: "5:44",
  105: "13:19",
  106: "6:17",
  107: "11:31",
  108: "12:50",
  109: "14:08",
  110: "7:02",
  111: "14:39",
  112: "16:20",
  113: "13:50",
  114: "4:41",
}

slide_transitions_ml_004_human_readable = {
1: ["0:20", "0:41", "4:10", "4:35"],
2: ["0:24", "2:33", "4:05"],
3: ["0:17", "2:59", "6:53", "10:22"],
4: ["0:13", "1:15", "2:36", "3:51", "5:25", "6:29", "9:49", "12:25"],
5: ["0:11", "1:52"],
6: ["0:10", "0:47"],
7: ["0:12", "1:34"],
8: ["0:31", "0:49", "1:57", "2:39", "3:24"],
11: ["0:41", "2:13", "5:16"],
10: ["0:!5", "1:19", "5:39", "9:06"],
9: ["0:23", "0:59", "3:24", "4:33", "4:51", "5:34", "7:47"],
12: ["0:11", "2:46", "4:52"],
13: ["0:12", "4:57"],
14: ["0:13"],
15: ["0:13", "2:26", "5:03"],
16: ["0:28", "2:46", "5:12"],
17: ["0:18", "2:32", "4:51"],
18: ["0:13", "7:29"],
19: ["0:12", "0:27", "5:06"],
20: ["0:20", "1:56"],
21: ["0:13", "3:16", "5:39"],
22: ["0:11", "0:29", "4:28"],
23: ["0:27", "2:16", "5:21"],
24: ["0:12", "0:59", "3:44", "5:59", "11:27"],
25: ["0:33", "2:12"],
26: ["3:15"], # tutorial
27: ["0:22"], # tutorial
28: ["0:19"], # tutorial
29: ["0:53"], # tutorial https://class.coursera.org/ml-004/lecture/29
31: ["0:12", "9:01", "9:14", "12:17"], # tutorial
30: ["1:32", "5:40", "6:20"], # tutorial
32: ["0:15"], # tutorial
33: ["0:18", "2:26", "6:29"],
34: ["0:15", "3:17"],
35: ["0:18", "4:39"],
58: ["1:01", "4:33", "8:31", "9:20"],
36: ["0:22", "3:54", "5:54"],
37: ["0:31", "1:41", "5:42", "8:39", "10:43", "11:27"],
38: ["0:13", "1:33", "2:18", "5:16"],
39: ["0:39", "4:24", "7:37"],
40: ["0:36", "2:44", "6:05"],
41: ["0:17", "0:41", "5:20", "8:00"],
42: ["0:36", "2:17"],
43: ["0:43", "4:54", "5:53", "6:20"],
44: ["0:42", "2:16", "4:23"],
45: ["0:13", "1:19", "2:42", "5:32", "7:41"],
46: ["0:29", "5:57", "9:48"],
47: ["0:17", "2:10"],
48: ["0:10", "5:56", "6:20"],
49: ["0:29", "2:10"],
50: ["0:21", "3:00"],
51: ["0:13", "1:01", "2:34", "7:57"],
52: ["1:36", "2:07", "5:06", "6:45"],
53: ["0:20", "2:03", "5:28"],
54: ["1:53", "6:26", "8:56"],
55: ["0:12", "1:01", "4:40"],
56: ["0:21", "4:10", "7:21", "9:27"],
57: ["0:14"],
59: ["1:09", "4:41"],
60: ["0:16", "1:13", "3:27", "4:49"],
61: ["0:36", "1:38", "6:26", "8:11", "8:49"],
62: ["0:51", "1:31", "4:13"],
63: ["0:22", "2:19", "3:28", "6:41"],
64: ["0:24", "4:59", "8:16"],
65: ["0:21", "3:15"],
66: ["0:55", "1:38", "5:05"],
67: ["0:18", "3:00", "6:49"],
68: ["0:36", "4:10"],
69: ["0:28", "7:06"],
70: ["0:58", "4:21", "7:44"],
71: ["1:28", "3:01", "7:53"],
72: ["0:17", "2:31", "4:43"],
73: ["0:20", "5:55", "11:20"], # optional
74: ["0:16", "2:18", "5:45", "8:22"],
75: ["0:22", "2:12", "5:35", "12:44"],
76: ["0:11", "4:34", "8:34", "14:25"],
77: ["0:14", "0:46", "1:52"],
78: ["0:26", "3:42", "4:26", "9:59"],
79: ["0:49", "4:10"],
80: ["0:11", "0:38", "3:19", "5:19"],
81: ["0:43", "1:32"],
82: ["0:33", "6:10", "8:45"],
83: ["0:30", "1:42", "2:37"],
84: ["0:20", "2:42", "6:30"],
85: ["0:13", "1:38", "5:00", "9:19", "11:51"],
86: ["0:28", "4:26", "8:45"],
87: ["0:40"],
88: ["0:17", "5:36", "6:55", "9:39"],
89: ["0:24", "2:20", "4:04"],
90: ["0:31", "3:36", "5:50"],
91: ["0:10", "7:27"],
92: ["0:19", "3:18", "7:09"],
93: ["0:47", "5:20"],
95: ["0:33", "3:43", "5:28", "5:45", "9:18"],
96: ["0:25", "4:00", "5:56"], # optional
97: ["0:20", "1:51", "3:17", "6:37"],
98: ["3:07"],
99: ["0:31", "10:06", "11:24"],
100: ["0:20"],
101: ["0:21", "5:58"],
102: ["0:29", "1:16"],
103: ["0:18", "3:44"],
104: ["0:32", "1:20"],
105: ["0:37", "3:55", "9:23"],
106: ["0:18", "2:49"],
107: ["0:26", "3:48", "8:27"],
108: ["0:51", "6:35"],
109: ["1:18", "6:39", "8:08", "10:54"],
110: ["1:00", "3:04", "4:47"],
111: ["0:31", "1:58", "3:13", "6:03", "13:25"],
112: ["1:00", "1:13", "4:18", "5:27", "7:30"],
113: ["0:59", "7:31", "9:22"],
114: ["0:16"],
}

in_video_quiz_times_ml_004_human_readable = {
  1: [],
  2: ["3:14"],
  3: ["11:18"],
  4: ["13:00"],
  5: ["4:38"],
  6: ["2:12"],
  7: ["6:52"],
  8: [],
  11: ["10:48"],
  10: ["8:04"],
  9: ["9:04"],
  12: [],
  13: ["2:26", "6:16"],
  14: ["1:51", "4:01", "6:40"],
  15: ["5:15", "7:28"],
  16: ["7:33"],
  17: ["8:39"],
  18: ["9:38"],
  19: ["3:24"],
  20: ["1:21"],
  21: ["8:34"],
  22: ["6:51"],
  23: ["6:35"],
  24: ["8:44"],
  25: [],
  26: [],
  27: [],
  28: [],
  29: [],
  31: [],
  30: ["13:07"],
  32: [],
  33: ["7:07"],
  34: ["5:38"],
  35: ["9:47"],
  58: ["0:10", "10:40"],
  36: ["8:43", "9:29"],
  37: ["13:14"],
  38: ["6:01"],
  39: ["6:03"],
  40: ["7:59"],
  41: ["3:42"],
  42: ["3:54"],
  43: ["8:54"],
  44: [],
  45: ["11:42"],
  46: ["10:51"],
  47: ["6:15"],
  48: ["2:31"],
  49: ["3:31"],
  50: ["6:43"],
  51: ["11:27"],
  52: ["12:11"],
  53: ["3:48"],
  54: ["5:01", "11:19"],
  55: ["6:15"],
  56: ["11:58"],
  57: [],
  59: ["5:31"],
  60: ["2:47"],
  61: ["11:22"],
  62: ["7:08"],
  63: ["7:47"],
  64: ["11:43"],
  65: ["6:01"],
  66: ["7:47"],
  67: ["9:06"],
  68: ["9:45"],
  69: ["12:59"],
  70: ["10:26"],
  71: ["13:51"],
  72: ["7:12"],
  73: ["19:26"],
  74: ["11:02"],
  75: ["15:31"],
  76: ["12:50"],
  77: ["3:05"],
  78: ["7:12"],
  79: ["6:24"],
  80: ["7:20"],
  81: ["4:29"],
  82: ["9:47"],
  83: ["5:00"],
  84: ["8:40"],
  85: ["14:21"],
  86: ["9:57"],
  87: ["3:16"],
  88: ["12:08"],
  89: ["7:22"],
  90: ["9:56"],
  91: ["4:33"],
  92: ["10:11"],
  93: ["7:02"],
  95: ["11:50"],
  96: ["13:19"],
  97: ["13:43"],
  98: ["7:44"],
  99: ["6:13"],
  100: ["7:07"],
  101: ["8:06"],
  102: ["5:11"],
  103: ["8:18"],
  104: ["3:24"],
  105: ["13:07"],
  106: ["5:46"],
  107: ["10:58"],
  108: ["12:04"],
  109: ["13:29"],
  110: ["6:37"],
  111: ["10:44"],
  112: ["9:17", "15:25"],
  113: ["12:33"],
  114: [],
}

video_lengths_crypto_009_human_readable = {
  1: "10:34",
  2: "15:51",
  3: "18:49",
  67: "18:07",
  66: "13:49",
  4: "18:33",
  5: "19:47",
  6: "23:14",
  7: "19:38",
  8: "24:54",
  9: "15:31",
  10: "10:54",
  12: "16:44",
  13: "21:59",
  14: "19:41",
  15: "16:03",
  16: "13:33",
  17: "11:44",
  18: "11:30",
  19: "07:13",
  39: "22:50",
  20: "16:13",
  21: "09:19",
  22: "15:15",
  23: "09:58",
  24: "19:41",
  25: "08:39",
  26: "15:26",
  27: "10:53",
  28: "14:37",
  29: "11:34",
  30: "08:08",
  31: "07:04",
  32: "08:28",
  33: "12:53",
  34: "05:13",
  35: "12:05",
  36: "20:17",
  37: "17:39",
  38: "14:06",
  40: "09:49",
  41: "13:35",
  42: "14:33",
  43: "20:28",
  44: "14:25",
  45: "12:13",
  46: "11:11",
  47: "11:18",
  48: "19:00",
  49: "10:56",
  50: "14:15",
  51: "18:04",
  52: "17:08",
  53: "12:34",
  54: "18:39",
  55: "15:39",
  56: "10:24",
  57: "17:34",
  58: "21:07",
  59: "16:35",
  60: "13:55",
  61: "19:29",
  62: "13:11",
  63: "10:20",
  64: "11:44",
  65: "05:19",
}

video_lengths_ml_003_human_readable = {
  1: "06:54",
  2: "07:14",
  3: "12:29",
  4: "14:13",
  5: "08:10",
  6: "08:12",
  7: "11:09",
  8: "08:48",
  11: "11:30",
  10: "11:50",
  9: "10:20",
  12: "05:49",
  13: "08:45",
  14: "06:53",
  15: "13:39",
  16: "11:09",
  17: "09:02",
  18: "11:12",
  19: "08:22",
  20: "05:04",
  21: "08:51",
  22: "08:58",
  23: "07:39",
  24: "16:17",
  25: "05:58",
  26: "13:59",
  27: "16:07",
  28: "13:14",
  29: "09:38",
  31: "12:55",
  30: "13:48",
  32: "03:33",
  33: "08:08",
  34: "07:24",
  35: "14:49",
  58: "11:25",
  36: "10:14",
  37: "14:06",
  38: "06:15",
  39: "09:42",
  40: "10:10",
  41: "10:40",
  42: "08:33",
  43: "09:35",
  44: "07:47",
  45: "12:01",
  46: "11:46",
  47: "07:15",
  48: "10:20",
  49: "03:51",
  50: "06:43",
  51: "11:59",
  52: "12:44",
  53: "07:47",
  54: "11:37",
  55: "06:51",
  56: "13:23",
  57: "06:30",
  59: "05:50",
  60: "07:35",
  61: "12:03",
  62: "07:42",
  63: "11:20",
  64: "11:53",
  65: "06:50",
  66: "09:29",
  67: "13:11",
  68: "11:35",
  69: "14:05",
  70: "11:09",
  71: "14:47",
  72: "10:36",
  73: "19:41",
  74: "15:44",
  75: "15:43",
  76: "21:02",
  77: "03:16",
  78: "12:32",
  79: "07:04",
  80: "07:49",
  81: "08:22",
  82: "10:09",
  83: "05:27",
  84: "09:05",
  85: "15:13",
  86: "10:30",
  87: "03:54",
  88: "12:48",
  89: "07:38",
  90: "10:27",
  91: "12:02",
  92: "13:07",
  93: "07:36",
  95: "12:17",
  96: "13:45",
  97: "14:03",
  98: "07:54",
  99: "14:31",
  100: "10:14",
  101: "08:26",
  102: "08:27",
  103: "08:30",
  104: "05:44",
  105: "13:19",
  106: "06:17",
  107: "11:31",
  108: "12:50",
  109: "14:08",
  110: "07:02",
  111: "14:39",
  112: "16:20",
  113: "13:50",
  114: "04:41",
}

talking_heads_ml_004_human_readable = {
  1: [("0:03", "0:19"), ("0:46", "2:52")],
  13: [("0:03", "0:10")],
  46: [("0:09", "0:29")],
  47: [("0:09", "0:16")],
  48: [("0:03", "0:09")],
}

slides_ml_004_human_readable = {
  1: [("2:53", "4:10"), ("4:37", "6:54")],
  13: [("0:11", "2:25"), ("2:26", "4:56"), ("4:57", "6:15"), ("6:16", "8:45")],
  46: [("0:30", "5:57"), ("5:58", "9:47"), ("9:48", "10:50")],
  47: [("0:17", "2:09"), ("2:10", "6:14"), ("6:16", "7:15")],
  48: [("0:10", "2:31"), ("2:32", "5:55"), ("5:56", "6:19"), ("6:20", "10:20")],
  68: [("0:36", "4:09"), ("4:10", "9:45")],
  112: [("1:00", "1:11"), ("1:12", "4:17"), ("4:18", "5:26"), ("5:27", "7:29"), ("7:30", "9:17"), ("9:18", "15:25")],
}

optional_lectures = frozenset([13, 14, 15, 16, 17, 18, 25, 73, 96, 97])
tutorial_lectures = frozenset([26, 27, 28, 29, 31, 30, 32])


video_lengths_ml_004 = { k: timeToSeconds(v) for k,v in video_lengths_ml_004_human_readable.iteritems() }
video_lengths_crypto_009 = { k: timeToSeconds(v) for k,v in video_lengths_crypto_009_human_readable.iteritems() }
video_lengths_ml_003 = { k: timeToSeconds(v) for k,v in video_lengths_ml_003_human_readable.iteritems() }
in_video_quiz_times_ml_004 = { k: [timeToSeconds(x) for x in v] for k,v in in_video_quiz_times_ml_004_human_readable.iteritems() }
slides_ml_004 = { k: [TRange(x,y) for x,y in v] for k,v in slides_ml_004_human_readable.iteritems() }
talking_heads_ml_004 = { k: [TRange(x,y) for x,y in v] for k,v in talking_heads_ml_004_human_readable.iteritems() }








