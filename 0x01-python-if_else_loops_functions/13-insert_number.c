#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: linked list
 * @number: the number to make the new node
 * Return: the address of the new node, or NULL if it failed
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *old;
	listint_t *new;
	listint_t *node;

	if (*head == NULL)
		return (NULL);
	node = malloc(sizeof(listint_t *));
	if (node == NULL)
		return (NULL);
	node->next = NULL;
	node->n = number;

	old = *head;
	new = *head;
	while (old->next != NULL)
	{
		old = old->next;
		if (old->n >= number)
		{
			new->next = node;
			node->next = old;
			return (node);
		}
		new = new->next;
	}
	return (NULL);
}
