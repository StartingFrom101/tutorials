/** @odoo-module **/
import { Component, xml } from "@odoo/owl";

export class Todo extends Component {
    
}

Todo.template = 'owl_playground.Todo';
Todo.props =  {
    id: {type: Number}, 
    description: {type: String},
    done: {type: Boolean},
}