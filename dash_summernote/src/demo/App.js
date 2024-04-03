/* eslint no-magic-numbers: 0 */
import React, { useState } from 'react';

import { DashSummernote } from '../lib';

const App = () => {

    const [state, setState] = useState({value:'', label:'Type Here'});
    const setProps = (newProps) => {
            setState(newProps);
        };

    return (
        <div>
            <DashSummernote
                setProps={setProps}
                {...state}
            />
        </div>
    )
};


export default App;
