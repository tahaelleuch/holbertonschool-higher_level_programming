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
	listint_t *node;

	if (*head == NULL)
		return (NULL);
	node = malloc(sizeof(listint_t *));
	if (node == NULL)
		return (NULL);
	node->next = NULL;
	node->n = number;
	old = *head;
	if (old == NULL || old->n >= number)
	{
		node->next = *head;
		*head = node;
		return (node);
	}
	while (old->next != NULL)
	{
		if (old->next->n >= number)
		{
			node->next = old->next;
			old->next = node;
			return (node);
		}
		old = old->next;
	}
	old->next = node;
	return (node);
}
