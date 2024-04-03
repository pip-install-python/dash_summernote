# AUTO GENERATED FILE - DO NOT EDIT

export dashsummernote

"""
    dashsummernote(;kwargs...)

A DashSummernote component.

Keyword arguments:
- `id` (String; optional)
- `height` (Real; optional)
- `toolbar` (Array; optional)
- `value` (String; optional)
"""
function dashsummernote(; kwargs...)
        available_props = Symbol[:id, :height, :toolbar, :value]
        wild_props = Symbol[]
        return Component("dashsummernote", "DashSummernote", "dash_summernote", available_props, wild_props; kwargs...)
end

