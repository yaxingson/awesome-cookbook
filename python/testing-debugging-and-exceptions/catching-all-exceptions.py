from warnings import warn

class Buffer:
  def __init__(self):
    messages = [
      'Buffer() is deprecated due to security and usability issues.', 
      'Please use the Buffer.alloc() or Buffer.allocUnsafe() methods instead'  
    ]
    warn(''.join(messages), DeprecationWarning)

  @staticmethod
  def alloc():
    pass

  @staticmethod
  def allocUnsafe():
    pass

Buffer()
