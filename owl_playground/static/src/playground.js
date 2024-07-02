/** @odoo-module **/

import { Component, useState, App } from "@odoo/owl";
import { Counter } from "./counter/counter";
import { TodoList } from "./todolist/todolist";

export class Playground extends Component {
    static template = "owl_playground.playground";

    static components = {Counter, TodoList};

    setup() {  
    }
}
