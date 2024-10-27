EmpUsers: Name, EMails etc
Workdetail: Title (e.g photography, editing, marketing etc)
Products: Sku, title, date_added, date_completed (whole pipeling is realted to product work and users)
Progress: product_id, user_id, work_id, status (ongoing or complete)(work_id will change based on which work is complete)
EmpPosition: title (Photographer, editor, manager etc)
userPosition: user_id, position_id, work_id (in case user work in multiple positions)
progressUpdated: product_id, user_id, date_changed, status_changed_to, work_id (this is to keep log of every change that can be used for user reports and analytics)

{% for product_sku, progress_entries in progress_data.items %}

<tr>
<td>{{ product_sku }}</td>
<!-- Display the product name from the first entry -->
{% for progress in progress_entries %} {% for work in allowed_work %}
<!-- {{ progress.workflow_stage.title }} -> {{ work.work.title }} -->
{% if progress.workflow_stage.title == work.work.title %}
<td><select class="dropdown" name="progress_status"
data-product-id="{{ progress.product.id }}"
data-progress-row="{{ progress.id }}"
data-work-id="{{ progress.workflow_stage.id }}"
onchange="updateStatus(this)"
{% if progress.status == "completed" %} disabled = true {% endif %}>
<option value="not_started" {% if progress.status == "not_started" %}selected{% endif %}>Not Started</option>
<option value="ongoing" {% if progress.status == "ongoing" %}selected{% endif %}>Ongoing</option>
<option value="completed" {% if progress.status == "completed" %}selected{% endif %}>Completed</option>
</select>{{ progress.user.name }}</td>
{% else %}
<td></td>
{% endif %} {% endfor %}
<!-- Display status or any other field you want from the Progress model -->
{% endfor %}
</tr>
{% empty %}
<td colspan="3" class="no-data">No progress data available.</td>
{% endfor %}

    <h1>Product Workflow Progress</h1>
    <!-- <a class="btn-save" href="#" id="save-button">Save Progress</a> -->
    <form method="POST" action="{% url 'logout' %}" class="logout-form">
      {% csrf_token %}
      <button type="submit" class="logout-button">Logout</button>
    </form>
    <table>
      <thead>
        <tr>
          <th>Product SKU</th>
          {% for work in allowed_work %}
          <th>{{ work.work }}</th>
          {% endfor %}
        </tr>
      </thead>
      <tbody>
        {% for product_sku, progress_entries in progress_data.items %}
        <tr>
          <td>{{ product_sku }}</td>
          <!-- Display the product name from the first entry -->
          {% for progress in progress_entries %}
          {% if progress %}
            <td><select class="dropdown" name="progress_status"
              data-product-id="{{ progress.product.id }}"
              data-progress-row="{{ progress.id }}"
              data-work-id="{{ progress.workflow_stage.id }}"
              onchange="updateStatus(this)"
              {% if progress.status == "completed" %} disabled = true {% endif %}>
                  <option value="not_started" {% if progress.status == "not_started" %}selected{% endif %}>Not Started</option>
                  <option value="ongoing" {% if progress.status == "ongoing" %}selected{% endif %}>Ongoing</option>
                  <option value="completed" {% if progress.status == "completed" %}selected{% endif %}>Completed</option>
              </select>{{ progress.user.name }}</td>
          {% else %}
          <td></td>
          {% endif %}
          {% endfor %}
        </tr>
        {% empty %}
        <td colspan="3" class="no-data">No progress data available.</td>
        {% endfor %}
      </tbody>
    </table>
