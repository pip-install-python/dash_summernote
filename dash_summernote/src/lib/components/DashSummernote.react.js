import React, { useEffect, useRef } from 'react';
import PropTypes from 'prop-types';
import ReactSummernote from 'react-summernote';
import 'react-summernote/dist/react-summernote.css';
import 'bootstrap/js/dist/modal';
import 'bootstrap/js/dist/dropdown';
import 'bootstrap/js/dist/tooltip';
import 'bootstrap/dist/css/bootstrap.css';

const DashSummernote = (props) => {
    const {id, setProps, value, toolbar, height} = props;

    return (
        <ReactSummernote
            id={id}
            value={value}
            options={{
                height: height,
                dialogsInBody: true,
                toolbar: toolbar
            }}
            onChange={(content) => {
                setProps({ value: content });
            }}
        />
    );
}

DashSummernote.defaultProps = {};

DashSummernote.propTypes = {
    id: PropTypes.string,
    value: PropTypes.string,
    setProps: PropTypes.func,
    toolbar: PropTypes.array,
    height: PropTypes.number
};

export default DashSummernote;