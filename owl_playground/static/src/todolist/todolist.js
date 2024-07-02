/** @odoo-module */

import { Todo } from "../todo";

import { Component, useState, onMounted, useRef } from "@odoo/owl";

export class TodoList extends Component {
    setup() {
        this.todoList = useState([]);
        const ref = useRef("todoInput");
        onMounted(() => {ref.el.focus()});
    }

    addTodo(event) {
        if (event.keyCode === 13 && event.target.value != "") {
            this.todoList.push({
                id: this.todoList.length + 1,
                description: event.target.value,
                done: false,
            });
            event.target.value = "";
        }
    }
}

TodoList.components = { Todo };
TodoList.template = "owl_playground.TodoList";