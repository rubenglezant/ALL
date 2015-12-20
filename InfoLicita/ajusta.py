s = "";
i = 0;
with open("out.txt") as f:
    for line in f:
	i = i + 1;
	if (i == 38):
		print (s);
		i = 0;
		s = "";
	else:		
		s = s + line.rstrip('\n') + "|";

	


