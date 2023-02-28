# items = {
#     "computer": 10,
#     "printer": 8,
#     "mouse": 15,
#     "webcam": 12
# }
#
# # print(items.get("microphone",0))
#
# quantity = items.setdefault("microphone",0)
# print(items)
custom_dict = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
}
# devices_list = ["phone", "tablet", "computer", "TV"]
#
# new_dict = {}.fromkeys(devices_list,0)
# print(new_dict)
custom_list = [10, "one", "two", "ten", 20, 30, "five", 40, "nine", 50]
def group_types(p_list):
    output_dict = dict.fromkeys(p_list)
    for key in output_dict:
        if isinstance(key,int):
            output_dict[key] = "Integer"
        else:
            output_dict[key] = "String"
    print(output_dict)

print(group_types(custom_list))
