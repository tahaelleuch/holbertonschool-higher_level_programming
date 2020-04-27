#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - check if linked list cycle
 * list: linked list to check
 * Return: 0 if no cycle 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *new, *check;

	if (list == NULL)
		return (0);
	new = list;
	check = list;
	while (new && new->next)
	{
		new = new->next->next;
		check = check->next;
		if (new == check)
			return (1);
	}
	return (0);
}
