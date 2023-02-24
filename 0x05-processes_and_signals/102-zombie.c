#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

/**
 * infinite_while - Infinite loop
 * Return: Nothing
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - entry point
 * Return: 0 (success)
 */

int main(void)
{
	pid_t p;
	int i;

	for (i = 0; i < 5; i++)
	{
		p = fork();
		if (p < 0)
		{
			fprintf(stderr, "Fork failed\n");
			exit(1);
		}
		else if (p == 0)
		{
			exit(0);
		}
		else
		{
			printf("Zombie process created, PID: %d\n", p);
		}
	}

	infinite_while();

	return (0);
}
