#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
/*
 * main- check the code and create a zombie process
 * Return: Always 0
 */

int main(void)
{
	pid_t child_pid;

	child_pid = fork();
	if (child_pid > 0)
	{
		sleep(60);
	}
	else
	{
		exit(0);
	}
	return (0);
}
