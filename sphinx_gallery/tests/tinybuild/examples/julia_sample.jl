#=
Julia example
=============

An example for code written in Julia.
=#

function sphere_vol(r)
    return 4/3 * π * r^3
end

# %%
# This should work in notebook mode, at least
println(sphere_vol(3))

#%%
# Here's a subsection about ϕ
# ---------------------------

ϕ = (1 + √5)/2
