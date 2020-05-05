#include "lists.h"
#include <stdio.h>
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: the header of the linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/
int is_palindrome(listint_t **head)
{
	listint_t *new;
	int arr[100];
	int i = 0;
	int j;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	new = *head;
	while (new->next != NULL)
	{
		arr[i] = new->n;
		new = new->next;
		i++;
	}
	arr[i] = new->n;
	for (j = 0; j <= j / 2; j++)
	{
		if (arr[j] != arr[i - j - 1])
			return (0);
	}
	return (1);
}
