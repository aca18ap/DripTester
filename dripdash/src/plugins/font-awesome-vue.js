import Vue from "vue";

import { library } from "@fortawesome/fontawesome-svg-core";
import {
  faPowerOff,
  faAngleDown,
  faCog,
  faEllipsisV,
  faSyncAlt,
  faPencilAlt,
  faCheckCircle,
  faTimesCircle,
  faExclamationCircle,
  faSave,
  faTimes,
  faArrowUp,
  faArrowDown,
  faPlus,
  faTrashAlt,
  faUsers,
  faMicrochip
} from "@fortawesome/free-solid-svg-icons";
import { faQuestionCircle as farQuestionCircle } from "@fortawesome/free-regular-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

// Add the required icons to keep the bundle small.
library.add(
  faPowerOff,
  faAngleDown,
  faCog,
  faEllipsisV,
  faSyncAlt,
  faPencilAlt,
  faCheckCircle,
  faTimesCircle,
  faExclamationCircle,
  farQuestionCircle,
  faSave,
  faTimes,
  faArrowUp,
  faArrowDown,
  faPlus,
  faTrashAlt,
  faUsers,
  faMicrochip
);

Vue.component("font-awesome-icon", FontAwesomeIcon);
