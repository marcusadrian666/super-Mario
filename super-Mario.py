import random

def print_map(player_pos, enemy_pos, star_pos, life_count):
    for i in range(5):
        for j in range(10):
            if (i, j) == player_pos:
                print('M', end='')
            elif (i, j) == enemy_pos:
                print('E', end='')
            elif (i, j) == star_pos:
                print('*', end='')
            else:
                print('-', end='')
        print()
    print("生命值:", life_count)

def move_player(player_pos, direction):
    x, y = player_pos
    if direction == 'w' and x > 0:
        x -= 1
    elif direction == 's' and x < 4:
        x += 1
    elif direction == 'a' and y > 0:
        y -= 1
    elif direction == 'd' and y < 9:
        y += 1
    return x, y

def move_enemy(enemy_pos):
    x, y = enemy_pos
    x += random.randint(-1, 1)
    y += random.randint(-1, 1)
    x = max(0, min(x, 4))
    y = max(0, min(y, 9))
    return x, y

def main():
    print("欢迎来到超级马里奥游戏！")
    player_pos = (4, 0)
    enemy_pos = (random.randint(1, 4), random.randint(5, 9))
    star_pos = (random.randint(1, 4), random.randint(5, 9))
    life_count = 3

    while True:
        print_map(player_pos, enemy_pos, star_pos, life_count)

        if player_pos == (0, 9):
            print("恭喜你获胜！")
            break

        if life_count == 0:
            print("生命值用尽，游戏结束。")
            break

        direction = input("请输入方向(w上/s下/a左/d右)，或者输入q退出游戏：").lower()

        if direction == 'q':
            print("游戏结束。")
            break

        if direction not in ['w', 's', 'a', 'd']:
            print("无效的输入，请重新输入。")
            continue

        player_pos = move_player(player_pos, direction)
        enemy_pos = move_enemy(enemy_pos)

        if player_pos == enemy_pos:
            print("你被敌人抓住了！")
            life_count -= 1

        if player_pos == star_pos:
            print("你获得了一个星星！生命值恢复一点。")
            life_count = min(3, life_count + 1)

if __name__ == "__main__":
    main()
