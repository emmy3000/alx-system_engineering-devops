#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

/**
 * main - program creates 5 processes eventually
 * becoming zombie processes.
 *
 * Return: Always 0
 */
int main(void)
{
	int i;
	pid_t pid;

	for (i = 0; i < 5; i++)
	{
		pid = fork();

		if (pid == 0)
			exit(0);
		else if (pid < 0)
		{
			fprintf(stderr, "Fork failed\n");
			exit(1);
		}
		else
		{
			printf("Zombie process created, PID %d\n", pid);
			sleep(1);
		}
	}

	while (1)
		sleep(1);

	return (0);
}
