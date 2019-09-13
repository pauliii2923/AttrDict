
class AttrDict(dict):
  def __recurse__(self):
    

    dict_keys_to_change = []
    
    for a,b in self.items():
      if "values" in dir(b):
        dict_keys_to_change.append(a)
    for a in dict_keys_to_change:
      self[a] = AttrDict(self[a])



    list_keys_to_change = []
    
    for a,b in self.items():
      if "append" in dir(b) and "extend" in dir(b):
        list_keys_to_change.append(a)
    for a in list_keys_to_change:
      self[a] = [AttrDict(i) if "values" in dir(i) else i for i in self[a]]
  

  def __getattr__(self, attr):
    self.__recurse__()
    return self[attr]
  

  def __setattr__(self, attr, value):
    self[attr] = value
    self.__recurse__()
      

  def items(self):
    d = []
    for k,v in super().items():
      if "values" in dir(v):
        d.append((k, AttrDict(v)))
      else:
        d.append((k, v))
    return d
  

  def get(self, *args):
    try: return self[args[0]]
    except:
      if len(args) == 2:
        return args[1]
      else:
        return self[args[0]]


  def copy(self):
    return AttrDict(self)
