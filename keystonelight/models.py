

class Token(dict):
  def __init__(self, id=None, user=None, tenant=None, *args, **kw):
    super(Token, self).__init__(id=id, user=user, tenant=tenant, *args, **kw)


class User(dict):
  def __init__(self, id=None, tenants=None, *args, **kw):
    if tenants is None:
      tenants = []
    super(User, self).__init__(id=id, tenants=tenants, *args, **kw)


class Tenant(dict):
  def __init__(self, id=None, *args, **kw):
    super(Tenant, self).__init__(id=id, *args, **kw)


class Role(dict):
  def __init__(self, id=None, *args, **kw):
    super(Role, self).__init__(id=id, *args, **kw)


class Extras(dict):
  def __init__(self, user=None, tenant=None, *args, **kw):
    super(Extras, self).__init__(user=User, tenant=tenant, *args, **kw)