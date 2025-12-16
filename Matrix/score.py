score = [["王飞", 89, 98, 89], ["刘洋", 92, 93, 87], ["胡大海", 96, 91, 92]]
res = sorted(score, key=lambda x: x[1] + x[2] + x[3], reverse=True)
if __name__ == "__main__":
    print(' '.join(r[0] for r in res))
