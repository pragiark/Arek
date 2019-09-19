def make_album(name, title, track=""):
	if track:
		cover = {"artist": name, "album": title, "Ilosc utworów": track}
	else:
		cover = {"artist": name, "album": title}

	print(cover)


while True:
	name = input("Podaj artustę/Zespół: (q to zakaończenie)")
	if name == "q":
		break
	title = input("Podaj album: (q to zakaończenie)")
	if title == "q":
		break

make_album(name,title)


