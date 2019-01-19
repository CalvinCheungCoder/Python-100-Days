import threading

# 当前线程对象
t = threading.current_thread()
print(t.name)

print(threading.active_count())

t = threading.main_thread()
print(t.name)