class User:
  def __init__(self, user_id):
    self.user_id = user_id

  def __repr__(self):
    return 'User({!r})'.format(self.user_id)

users = [User(23), User(5), User(99)]

sorted_users = sorted(users, key=lambda u: u.user_id)

print(sorted_users)

min_user = min(users, key=lambda u: u.user_id)
max_user = max(users, key=lambda u: u.user_id)

print(min_user)
print(max_user)
