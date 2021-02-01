def sandwitch_items(items):
    print("\nthe following items will be added to your sandwitch: ")
    for i in items:
        print(f"- {i}")

s_items = ['bun','chocolate','chesse','tomato']
s_items1 = ['bun','ham']
s_items2 = ['almonds','apricots','grapes']

sandwitch_items(s_items)
sandwitch_items(s_items1)
sandwitch_items(s_items2)

