

int main() {
	char arr[5];
	scanf("%s", arr);
	int ans = 1;

	if (arr[0] == 'c') ans *= 26;
	else ans *= 10;

	int i = 1;
	while (arr[i] == 'c' || arr[i] == 'd') {
		if (i >= 4) break;

		if (arr[i - 1] == arr[i]) {
			
			if (arr[i] == 'c') ans *= 25;
			else ans *= 9;
		}
		else {
			if (arr[i] == 'c') ans *= 26;  
			else ans *= 10;
		}
		i++;
	}
	printf("%d\n", ans);
	return 0;
}