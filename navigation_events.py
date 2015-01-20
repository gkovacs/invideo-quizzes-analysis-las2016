#!/usr/bin/env python
# md5: 44b41b92a30cb66d70f4abf9280aadd6
# coding: utf-8

class SeekEvent:
  def __init__(self, timestamp, start, end, paused):
    self.timestamp = timestamp
    self.start = start
    self.end = end
    self.event_type = 'seeked'
    self.paused = bool(paused)
    if self.end >= self.start:
      self.direction = 'forward'
    else:
      self.direction = 'back'
  def __str__(self):
    return dumps(self.__dict__)
  def __repr__(self):
    return str(self)

class SeekChain:
  def __init__(self, seek_events):
    assert len(seek_events) > 0
    self.seek_events = seek_events
    self.start = seek_events[0].start
    self.end = seek_events[-1].end
    self.event_type = 'seek_chain'
    if self.end >= self.start:
      self.direction = 'forward'
    else:
      self.direction = 'back'
    self.timestamp = seek_events[0].timestamp
    self.timestamp_end = seek_events[-1].timestamp
  def __str__(self):
    output = self.__dict__
    output['seek_events'] = [x.__dict__ for x in output['seek_events']]
    return dumps(output)
  def __repr__(self):
    return str(self)

class PlayEvent:
  def __init__(self, timestamp, start, playback_rate):
    self.timestamp = timestamp
    self.start = start
    self.playback_rate = playback_rate
    self.event_type = 'play'

class PlaySpan:
  def __init__(self, timestamp, timestamp_end, start, end, playback_rate):
    self.timestamp = timestamp
    self.timestamp_end = timestamp_end
    self.start = start
    self.end = end
    self.playback_rate = playback_rate
    self.event_type = 'play_span'
    if self.timestamp == None:
      raise DataException('PlaySpan timestamp cannot be None')
    if self.timestamp_end == None:
      raise DataException('PlaySpan timestamp_end cannot be None')
    if self.start == None:
      raise DataException('PlaySpan start cannot be None')
    if self.end == None:
      raise DataException('PlaySpan end cannot be None')
    if self.playback_rate == None:
      raise DataException('PlaySpan playback_rate cannot be None')
  def __str__(self):
    return '(' + str(self.start) + ', ' + str(self.end) + ')'
  def __repr__(self):
    return self.__str__()

class PauseEvent:
  def __init__(self, timestamp, start):
    self.timestamp = timestamp
    self.start = start
    self.event_type = 'pause'

class RateChangeEvent:
  def __init__(self, timestamp, start, playback_rate, paused):
    self.timestamp = timestamp
    self.start = start
    self.playback_rate = playback_rate
    self.event_type = 'ratechange'
    self.paused = bool(paused)

